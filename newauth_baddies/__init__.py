import json
import operator
from pkg_resources import resource_string
from flask import current_app, render_template_string, url_for, request, flash, redirect, abort, make_response, jsonify
from flask.ext.classy import FlaskView, route
from flask.ext.login import current_user
from newauth.eveapi import EveAPIQuery
from newauth.models import Group, Character


class Baddies(object):
    """Show your alliance/corporations members that are not in NewAuth"""

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        app.config.setdefault('BADDIES_ACCESS', [app.config['ADMIN_GROUP']])

        self.BaddiesView.register(app)

        # Registering to navbar
        app.navbar['extra'].append(('fa-ban', 'HR Baddies', 'BaddiesView:index', self.BaddiesView._can_access))

        self.app.logger.debug("Baddies is enabled.")

    class BaddiesView(FlaskView):

        route_base = '/extra/baddies'

        templates = {
            'index': resource_string(__name__, 'templates/index.html')
        }

        @staticmethod
        def _can_access():
            for group in current_app.config['BADDIES_ACCESS']:
                g = Group.query.filter_by(name=group).first()
                if not g:
                    raise Exception('Group {} from BADDIES_ACCESS not found.'.format(group))
                if current_user.is_member_of(g):
                    return True
            return False

        def index(self):
            corporations = []
            baddies = {}
            corporation_name = None
            for key in current_app.config['EVE']['keys']:
                api = EveAPIQuery(key_id=key[0], vcode=key[1])
                try:
                    api_info = api.get('account/APIKeyInfo')
                except Exception as e:
                    current_app.logger.exception(e)
                    flash('We could not get information from the key #{}.'.format(key[0]), 'danger')
                    break
                corporations.append({'value': api_info['characters']['row'][0]['corporationID'], 'name': api_info['characters']['row'][0]['corporationName']})
                if request.args.get('corporation_id') == str(api_info['characters']['row'][0]['corporationID']):
                    try:
                        members = api.get('corp/MemberTracking')['row']
                    except Exception as e:
                        current_app.logger.exception(e)
                        flash('We could not get information from the key #{}'.format(key[0]), 'danger')
                        break
                    characters = set([c.characterID for c in members])
                    characters_db = set([c.id for c in Character.query.filter_by(corporation_id=api_info['characters']['row'][0]['corporationID'])])
                    diff = characters.difference(characters_db)
                    baddies = [c for c in sorted(members, key=operator.attrgetter('name')) if c.characterID in diff]
                    corporation_name = api_info['characters']['row'][0]['corporationName']
            return render_template_string(self.templates['index'], corporations=corporations, baddies=baddies, corporation_name=corporation_name)



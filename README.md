NewAuth Baddies
================

Show your alliance/corporations members that are not in NewAuth

## Installation

You should be able to install this plugin to your virtualenv with a simple pip command:

    pip install https://github.com/j4lp/newauth_baddies.git

## Configuration

By default, only members of the `ADMIN_GROUP` will have access to the baddie list, you should add a list of **group names** to your settings.

You will also need a corporation key for each corporations you want to appear with the MemberList permission. Add these keys to the `EVE['keys']` configuration key as a tuple of (key_id, vcode).

## License

The MIT License (MIT)

Copyright (c) 2014 Adrien F

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

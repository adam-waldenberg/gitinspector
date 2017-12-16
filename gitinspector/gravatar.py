# coding: utf-8
#
# Copyright © 2013-2014 Ejwa Software. All rights reserved.
#
# This file is part of gitinspector.
#
# gitinspector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gitinspector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gitinspector. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
import hashlib

try:
	from urllib.parse import urlencode
except:
	from urllib import urlencode

from . import format
from . import gitinspector

def get_url(email, size=20):
	if gitinspector.github_usernames and email in gitinspector.github_usernames:
		return "https://github.com/" + gitinspector.github_usernames[email] + ".png?size=20"
	md5hash = hashlib.md5(email.encode("utf-8").lower().strip()).hexdigest()
	base_url = "https://www.gravatar.com/avatar/" + md5hash
	params = None

	if format.get_selected() == "html":
		params = {"default": "identicon", "size": size}
	elif format.get_selected() == "xml" or format.get_selected() == "json":
		params = {"default": "identicon"}

	return base_url + "?" + urlencode(params)

def get_username(email):
	if gitinspector.github_usernames and email in gitinspector.github_usernames:
		return gitinspector.github_usernames[email]
	return None

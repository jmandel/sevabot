from __future__ import absolute_import, division, unicode_literals

import re
import logging
import shlex
import settings

logger = logging.getLogger('sevabot')

class ChatLogger(object):

    @staticmethod
    def log(msg):
        print "\n".join(["LOGGING A MESSAGE", str(msg.Id), str(msg.Timestamp), str(msg.EditedTimestamp), msg.Chat.Description, msg.Sender.DisplayName, msg.Sender.FullName, msg.Body.encode('utf-8')])

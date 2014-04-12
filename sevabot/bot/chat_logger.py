from __future__ import absolute_import, division, unicode_literals

import re
import logging
import shlex
import settings
import pymongo

from pymongo import MongoClient
client = MongoClient(settings.MONGO_URL)

logger = logging.getLogger('sevabot')
messages = client['fhir-logs'].messages

class ChatLogger(object):

    @staticmethod
    def log(msg):
        m = {
            'chat_room_id': msg.Chat.Name,
            'chat_room_name': msg.Chat.FriendlyName,
            'message_id': msg.Id,
            'sent_at': msg.Datetime,
            'edited': msg.EditedTimestamp > 0 and True or False,
            'edited_at': msg.EditedDatetime,
            'user_skypename': msg.Sender.Handle,
            'user_fullname': msg.Sender.FullName,
            'body': msg.Body.encode('utf-8')
        }
        messages.insert(m)
        print "inserted", m, msg.EditedTimestamp

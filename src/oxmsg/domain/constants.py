"""Constant definitions, mostly property ids (PIDs) and property types (PTYPs)."""

# -- Property IDs - These names are formed by upper-snake-casing the Microsoft name for each
# -- property-id, dropping the "Tag" segment. E.g. "PidTagAttachSize" -> "PID_ATTACH_SIZE"

PID_ACCESS = 0x0FF4
PID_ACCESS_LEVEL = 0x0FF7
PID_ACKNOWLEDGEMENT_MODE = 0x0001
PID_ADDRESS_BOOK_FOLDER_PATHNAME = 0x8004
PID_ADDRESS_BOOK_HOME_MESSAGE_DATABASE = 0x8006
PID_ADDRESS_BOOK_IS_MEMBER_OF_DISTRIBUTION_LIST = 0x8008
PID_ADDRESS_BOOK_MANAGER_DISTINGUISHED_NAME = 0x8005
PID_ADDRESS_BOOK_MEMBER = 0x8009
PID_ADDRESS_TYPE = 0x3002
PID_ALTERNATE_RECIPIENT_ALLOWED = 0x0002
PID_ATTACHMENT_FLAGS = 0x7FFD
PID_ATTACHMENT_HIDDEN = 0x7FFE
PID_ATTACHMENT_LINK_ID = 0x7FFA
PID_ATTACH_CONTENT_ID = 0x3712
PID_ATTACH_DATA_BINARY = 0x3701
PID_ATTACH_ENCODING = 0x3702
PID_ATTACH_EXTENSION = 0x3703
PID_ATTACH_FILENAME = 0x3704
PID_ATTACH_FLAGS = 0x3714
PID_ATTACH_LONG_FILENAME = 0x3707
PID_ATTACH_METHOD = 0x3705
PID_ATTACH_MIME_SEQUENCE = 0x3710
PID_ATTACH_MIME_TAG = 0x370E
PID_ATTACH_NUMBER = 0x0E21
PID_ATTACH_RENDERING = 0x3709
PID_ATTACH_RENDERING_POSITION = 0x370B
PID_ATTACH_SIZE = 0x0E20
PID_ATTACH_TAG = 0x370A
PID_AUTHORIZING_USERS = 0x0003
PID_AUTO_FORWARDED = 0x0005
PID_AUTO_FORWARD_COMMENT = 0x0004
PID_BODY = 0x1000
PID_BODY_HTML = 0x1013
PID_CHANGE_KEY = 0x65E2
PID_CLIENT_SUBMIT_TIME = 0x0039
PID_CONTENT_CONFIDENTIALITY_ALGORITHM_ID = 0x0006
PID_CONTENT_CORRELATOR = 0x0007
PID_CONTENT_IDENTIFIER = 0x0008
PID_CONTENT_LENGTH = 0x0009
PID_CONTENT_RETURN_REQUESTED = 0x000A
PID_CONVERSATION_INDEX = 0x0071
PID_CONVERSATION_INDEX_TRACKING = 0x3016
PID_CONVERSATION_KEY = 0x000B
PID_CONVERSATION_TOPIC = 0x0070
PID_CONVERSION_EITS = 0x000C
PID_CONVERSION_WITH_LOSS_PROHIBITED = 0x000D
PID_CONVERTED_EITS = 0x000E
PID_CREATION_TIME = 0x3007
PID_CREATOR_ADDRESS_TYPE = 0x4022
PID_CREATOR_EMAIL_ADDRESS = 0x4023
PID_CREATOR_SIMPLE_DISPLAY_NAME = 0x4038
PID_DEFERRED_DELIVERY_TIME = 0x000F
PID_DELEGATION = 0x007E
PID_DELETE_AFTER_SUBMIT = 0x0E01
PID_DELIVER_TIME = 0x0010
PID_DISCARD_REASON = 0x0011
PID_DISCLOSURE_OF_RECIPIENTS = 0x0012
PID_DISPLAY_BCC = 0x0E02
PID_DISPLAY_CC = 0x0E03
PID_DISPLAY_NAME = 0x3001
PID_DISPLAY_TO = 0x0E04
PID_DISTRIBUTION_LIST_EXPANSION_HISTORY = 0x0013
PID_DISTRIBUTION_LIST_EXPANSION_PROHIBITED = 0x0014
PID_EMAIL_ADDRESS = 0x3003
PID_END_DATE = 0x0061
PID_ENTRY_ID = 0x0FFF
PID_EXCEPTION_END_TIME = 0x7FFC
PID_EXCEPTION_START_TIME = 0x7FFB
PID_EXPIRY_TIME = 0x0015
PID_FLAG_STATUS = 0x1090
PID_HAS_ATTACHMENTS = 0x0E1B
PID_HTML = 0x1013
PID_ICON_INDEX = 0x1080
PID_IMPLICIT_CONVERSION_PROHIBITED = 0x0016
PID_IMPORTANCE = 0x0017
PID_INITIAL_DETAILS_PANE = 0x3F08
PID_INSTANCE_KEY = 0x0FF6
PID_INTERNET_CODEPAGE = 0x3FDE
PID_INTERNET_MESSAGE_ID = 0x1035
PID_INTERNET_REFERENCES = 0x1039
PID_IN_REPLY_TO_ID = 0x1042
PID_LAST_MODIFICATION_TIME = 0x3008
PID_LAST_MODIFIER_NAME = 0x3FFA
PID_LATEST_DELIVERY_TIME = 0x0019
PID_LID_CONTACT_ITEM_DATA = 0x8007
PID_MESSAGE_CC_ME = 0x0058
PID_MESSAGE_CLASS = 0x001A
PID_MESSAGE_CODEPAGE = 0x3FFD
PID_MESSAGE_DELIVERY_ID = 0x001B
PID_MESSAGE_DELIVERY_TIME = 0x0E06
PID_MESSAGE_FLAGS = 0x0E07
PID_MESSAGE_LOCALE_ID = 0x3FF1
PID_MESSAGE_RECIPIENT_ME = 0x0059
PID_MESSAGE_SECURITY_LABEL = 0x001E
PID_MESSAGE_SIZE_EXTENDED = 0x0E08
PID_MESSAGE_SUBMISSION_ID = 0x0047
PID_MESSAGE_TO_ME = 0x0057
PID_NATIVE_BODY = 0x1016
PID_NON_RECEIPT_NOTIFICATION_REQUESTED = 0x0C06
PID_NORMALIZED_SUBJECT = 0x0E1D
PID_OBJECT_TYPE = 0x0FFE
PID_OBSOLETED_MESSAGE_IDS = 0x001F
PID_ORIGINALLY_INTENDED_RECIPIENT_NAME = 0x0020
PID_ORIGINALLY_INTENDED_RECIP_ADDRTYPE = 0x007B
PID_ORIGINALLY_INTENDED_RECIP_EMAIL_ADDRESS = 0x007C
PID_ORIGINAL_AUTHOR_ADDRESS_TYPE = 0x0079
PID_ORIGINAL_AUTHOR_EMAIL_ADDRESS = 0x007A
PID_ORIGINAL_AUTHOR_ENTRY_ID = 0x004C
PID_ORIGINAL_AUTHOR_NAME = 0x004D
PID_ORIGINAL_DELIVERY_TIME = 0x0055
PID_ORIGINAL_DISPLAY_BCC = 0x0072
PID_ORIGINAL_DISPLAY_CC = 0x0073
PID_ORIGINAL_DISPLAY_TO = 0x0074
PID_ORIGINAL_EITS = 0x0021
PID_ORIGINAL_MESSAGE_CLASS = 0x004B
PID_ORIGINAL_MESSAGE_ID = 0x1046
PID_ORIGINAL_SENDER_ADDRESS_TYPE = 0x0066
PID_ORIGINAL_SENDER_EMAIL_ADDRESS = 0x0067
PID_ORIGINAL_SENDER_ENTRY_ID = 0x005B
PID_ORIGINAL_SENDER_NAME = 0x005A
PID_ORIGINAL_SENDER_SEARCH_KEY = 0x005C
PID_ORIGINAL_SENSITIVITY = 0x002E
PID_ORIGINAL_SENT_REPRESENTING_ADDRESS_TYPE = 0x0068
PID_ORIGINAL_SENT_REPRESENTING_EMAIL_ADDRESS = 0x0069
PID_ORIGINAL_SENT_REPRESENTING_ENTRY_ID = 0x005E
PID_ORIGINAL_SENT_REPRESENTING_NAME = 0x005D
PID_ORIGINAL_SENT_REPRESENTING_SEARCH_KEY = 0x005F
PID_ORIGINAL_SUBJECT = 0x0049
PID_ORIGINAL_SUBMIT_TIME = 0x004E
PID_ORIGINATOR_CERTIFICATE = 0x0022
PID_ORIGINATOR_DELIVERY_REPORT_REQUESTED = 0x0023
PID_ORIGINATOR_RETURN_ADDRESS = 0x0024
PID_ORIGIN_CHECK = 0x0027
PID_OWNER_APPOINTMENT_ID = 0x0062
PID_PARENT_DISPLAY = 0x0E05
PID_PARENT_KEY = 0x0025
PID_PREDECESSOR_CHANGE_LIST = 0x65E3
PID_PRIORITY = 0x0026
PID_PROOF_OF_SUBMISSION_REQUESTED = 0x0028
PID_READ_RECEIPT_ENTRY_ID = 0x0046
PID_READ_RECEIPT_REQUESTED = 0x0029
PID_READ_RECEIPT_SEARCH_KEY = 0x0053
PID_RECEIPT_TIME = 0x002A
PID_RECEIVED_BY_ADDRESS_TYPE = 0x0075
PID_RECEIVED_BY_EMAIL_ADDRESS = 0x0076
PID_RECEIVED_BY_ENTRY_ID = 0x003F
PID_RECEIVED_BY_NAME = 0x0040
PID_RECEIVED_BY_SEARCH_KEY = 0x0051
PID_RECEIVED_REPRESENTING_ADDRESS_TYPE = 0x0077
PID_RECEIVED_REPRESENTING_EMAIL_ADDRESS = 0x0078
PID_RECEIVED_REPRESENTING_ENTRY_ID = 0x0043
PID_RECEIVED_REPRESENTING_NAME = 0x0044
PID_RECEIVED_REPRESENTING_SEARCH_KEY = 0x0052
PID_RECIPIENT_REASSIGNMENT_PROHIBITED = 0x002B
PID_RECIPIENT_TYPE = 0x0C15
PID_RECORD_KEY = 0x0FF9
PID_REDIRECTION_HISTORY = 0x002C
PID_REPLY_RECIPIENT_ENTRIES = 0x004F
PID_REPLY_RECIPIENT_NAMES = 0x0050
PID_REPLY_TIME = 0x0030
PID_REPORT = 0x0031
PID_REPORT_DISPOSITION = 0x0080
PID_REPORT_DISPOSITION_MODE = 0x0081
PID_REPORT_ENTRY_ID = 0x0045
PID_REPORT_NAME = 0x003A
PID_REPORT_SEARCH_KEY = 0x0054
PID_REPORT_TIME = 0x0032
PID_RESPONSE_REQUESTED = 0x0063
PID_ROW_ID = 0x3000
PID_RTF_COMPRESSED = 0x1009
PID_RTF_IN_SYNC = 0x0E1F
PID_SEARCH_KEY = 0x300B
PID_SECURITY = 0x0034
PID_SENDER_ADDRESS_TYPE = 0x0C1E
PID_SENDER_EMAIL_ADDRESS = 0x0C1F
PID_SENDER_ENTRY_ID = 0x0C19
PID_SENDER_NAME = 0x0C1A
PID_SENDER_SEARCH_KEY = 0x0C1D
PID_SENDER_SMTP_ADDRESS = 0x5D01
PID_SENSITIVITY = 0x0036
PID_SENT_REPRESENTING_ADDRESS_TYPE = 0x0064
PID_SENT_REPRESENTING_EMAIL_ADDRESS = 0x0065
PID_SENT_REPRESENTING_ENTRY_ID = 0x0041
PID_SENT_REPRESENTING_NAME = 0x0042
PID_SENT_REPRESENTING_SEARCH_KEY = 0x003B
PID_SMTP_ADDRESS = 0x39FE
PID_START_DATE = 0x0060
PID_STORE_SUPPORT_MASK = 0x340D
PID_STORE_UNICODE_MASK = 0x340F
PID_SUBJECT = 0x0037
PID_SUBJECT_MESSAGE_ID = 0x0038
PID_SUBJECT_PREFIX = 0x003D
PID_TNEF_CORRELATION_KEY = 0x007F
PID_TRANSPORT_MESSAGE_HEADERS = 0x007D


# -- Property Data Types - These are detailed in the MS-OXCDATA spec --

PTYP_BINARY = 0x0102
PTYP_BOOLEAN = 0x000B
PTYP_FLOATING_32 = 0x0004
PTYP_FLOATING_64 = 0x0005
PTYP_GUID = 0x0048
PTYP_INTEGER_16 = 0x0002
PTYP_INTEGER_32 = 0x0003
PTYP_MULTIPLE_INTEGER_32 = 0x1003
PTYP_MULTIPLE_STRING = 0x101F
PTYP_OBJECT = 0x000D
PTYP_STRING = 0x001F
PTYP_STRING8 = 0x001E
PTYP_TIME = 0x0040

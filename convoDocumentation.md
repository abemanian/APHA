#Definition of Conversation Output

##*'_id'*

Alphanumeric ID for the conversation

##*'last_activity_date'* 

Date and time that the last messasge occured. Format: "YYYY-MM-DDTHH:MM:SS.SSSZ"

##*'messages'*

Dictionary of the actual messages between the matches. Each message is its own dictionray with the following terms

####*'_id'*

Alphanumeric ID for specific message

####*'created_date'*

Date and time that the specific messasge occured? Format: "YYYY-MM-DDTHH:MM:SS.SSSZ"

####*'from'*

Alphanumeric ID for the user that sent the message

####*'match_id'*

Alphanumeric ID of the match (two user pairing)

####*'message'*

String of the message text

####*'sent_date'*

Date and time that the specific messasge reached the server? Unclear what the difference is from *created_date* Format: "YYYY-MM-DDTHH:MM:SS.SSSZ"

####*'timestamp'*

Numeric representation of the time. Unclear if its the *sent_date* or the *created_date&

####*'to'*

Alphanumeric ID for the user that is receiving the message

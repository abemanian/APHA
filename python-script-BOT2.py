import pynder

FBTOKEN = "CAAGm0PX4ZCpsBAGdLtovfqgf7Ft9QmAohXlYMgKGWrAQROBOFYCgKUtWh5qugEHnECwcqqe6KhtU24sHYxxMmXFJBKulKnualceZC8GQHZA8Bj0VfTQWGOioLO2OkwclhRDoTolEBdH0GeZCZAhXjnPNnqrWiNx3CwK9pMZAQ6WVwE9l2XpUqPyCxxtHhyVUZBWsDcZAIgsZCtDCeQ1JvuFmU"
FBID = "862872910496940"

BOT2 = pynder.Session(FBID, FBTOKEN)
print BOT2.nearby_users()

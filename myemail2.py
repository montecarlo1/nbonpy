from mailer import Mailer
from mailer import Message

message = Message(From="bobbylee0810@126.com",
                  To="912151131@qq.com")
message.Subject = "An HTML Email"
message.Html = """<p>Hi!<br>
   How are you?<br>
   Here is the <a href="http://www.python.org">link</a> you wanted.</p>"""

sender = Mailer('smtp.example.com',587)
sender.send(message)
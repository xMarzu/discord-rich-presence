from pypresence import Presence
import time
from datetime import datetime

rpc = Presence("Client ID Here")
rpc.connect()
rpc.update(state="The Wording Below details", details="Wordings Above State", large_image="Main Image Of Rich Presence", large_text="Text When Hovering Over Large Image", small_image="Small Image of Rich Presence",start=time.time())


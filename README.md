# TikTok X-Gorgon 0404
TikTok X-Gorgon and X-Khronos signature generator.
# Tiktok Video Downloader - https://taptik.app
# Example Usage 
```py
from signature import signature

sig = signature(params="", data="", cookies="").get_value()

print(f"X-Gorgon: {sig['X-Gorgon']} X-Khronos: {sig['X-Khronos']}")
```

# Analysis
```
Values (md5 hashed): URL Params, Post Data, and Cookies
URL Params are mostly always required, while the post data and cookies are not.
If one of these values are not given, thirty-two zeros will be returned.

Hashed string example: 
  Params Hash -> 9336ebf25087d91c818ee6e9ec29f8c1 
  No Data -> 00000000000000000000000000000  
  No Cookies -> 00000000000000000000000000000000000

Encrypted string example:
  Version -> 0404 
  Static hash -> b0d30000  
  Encrypted hash string -> 3f2892cbeb57387ccee15dbc3694a6f7df5311c6


TikTok decrypts X-Gorgon and determines if it's valid.
True -> Access to API
False -> Status code 200, but returns an empty response
```

# Contact
* Telegram: https://t.me/aithedev
* Discord: ai#4026

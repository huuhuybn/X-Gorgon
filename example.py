from signature import signature

sig = signature(params="", data="", cookies="").get_value()

print(f"X-Gorgon: {sig['X-Gorgon']} X-Khronos: {sig['X-Khronos']}")

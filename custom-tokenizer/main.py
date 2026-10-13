import tiktoken

encoder  = tiktoken.encoding_for_model("gpt-4o")

text = "This is totally Unbeleivable!!!"

tokensEncoded = encoder.encode(text)
totalTokens = len(tokensEncoded)
print(f"Tokens: {tokensEncoded}") # [2500, 382, 15108, 1367, 37111, 73462, 10880]
print(f"Total No of Tokens: {totalTokens}") # 7

tokensDecoded = encoder.decode([2500, 382, 15108, 1367, 37111, 73462, 10880])
print(f"Decoded Tokens: {tokensDecoded}")

print(f"15108: {encoder.decode([15108])}")
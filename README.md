## experiments in cryptology

### OTP - One Time Pad

A one-time pad is an encryption technique that offers perfect secrecy because the key must be at least as long as the message. Both parties have a copy of the key and just exclusive-or (XOR) each byte of the message with the respective byte in the key.

They cannot be cracked as long as the key is random and is never reused. They are impractical because if the 2 parties have a comm channel secret enough to send the key then they could just use that for the message in the first place.

More from [wikipedia](https://en.wikipedia.org/wiki/One-time_pad)
"""Encryption keys used by FreeStyle Libre 2 glucometers.

The following constants are key materials required to communicate with the FreeStyle
Libre 2 glucometers.

No copyright is claimed for these keys, as they are requisite constants that are part
of the device's communication protocol.

We assert these these keys do not constitute Technical Protection Measures for the
purpose of copyright protection, as they do not protect copyrighted material but
rather obfuscate the communication between two devices under the control of the user.
"""

AUTHORIZATION_ENCRYPTION_KEY = 0x360C0E171551821D7961F891197B52A1
AUTHORIZATION_MAC_KEY = 0x738F004CD1A80D16622DB2E0DB8C60D4
SESSION_ENCRYPTION_KEY = 0x9D42333D9DDD20A7164C2AB057F92EFD
SESSION_MAC_KEY = 0x12B0D868D117D7C8379DE50FA97A7BA0

import rsa_key as rsaKey
import rsa_ency as rsaEncy
import rsa_decy as rsaDecy
print("\n\t=> Rsa key generation\n\n")
rsaKey.main()
print("\n\t.........Rsa key generation ended..........\n\n\t=> Rsa encryption started\n\n")
rsaEncy.main()
print("\n\t.........Rsa encryption ended..............\n\n\t=> Rsa decryption started\n\n")
rsaDecy.main()
print("\n\t.........Rsa decryption ended..............")
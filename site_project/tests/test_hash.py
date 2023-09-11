from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

print(pwd_context.hash("hash"))

pwd_context1 = CryptContext(schemes=["bcrypt"], deprecated="auto")

p = pwd_context1.hash("hash")
print(pwd_context1.verify("hash", p))

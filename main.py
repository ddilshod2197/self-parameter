class Arxitektor:
    def __init__(self, ism, familiya, tajriba):
        self.ism = ism
        self.familiya = familiya
        self.tajriba = tajriba

    def info(self):
        return f"Ism: {self.ism}, Familiya: {self.familiya}, Tajriba: {self.tajriba} yil"

class GoogleArxitektor(Arxitektor):
    def __init__(self, ism, familiya, tajriba, google_tajriba):
        super().__init__(ism, familiya, tajriba)
        self.google_tajriba = google_tajriba

    def info(self):
        return super().info() + f", Google tajriba: {self.google_tajriba} yil"

class MetaArxitektor(Arxitektor):
    def __init__(self, ism, familiya, tajriba, meta_tajriba):
        super().__init__(ism, familiya, tajriba)
        self.meta_tajriba = meta_tajriba

    def info(self):
        return super().info() + f", Meta tajriba: {self.meta_tajriba} yil"

google_arxitektor = GoogleArxitektor("Ali", "Valiyev", 5, 3)
meta_arxitektor = MetaArxitektor("Vali", "Aliyev", 7, 2)

print(google_arxitektor.info())
print(meta_arxitektor.info())
```

Kodda `self` parametriga nima uchun kerakligini ko'rish uchun quyidagilar kabi qilib ko'ring:

- `self` parametriga kerak bo'lishi uchun klassga `__init__` metodi mavjud bo'lishi kerak.
- `self` parametriga kerak bo'lishi uchun klassga `__init__` metodi ichida `self` parametriga qo'llaniladigan atributlar mavjud bo'lishi kerak.
- `self` parametriga kerak bo'lishi uchun klassga `__init__` metodi ichida `self` parametriga qo'llaniladigan atributlar klassning boshqa metodlarida ham qo'llanilishi kerak.
- `self` parametriga kerak bo'lishi uchun klassga `__init__` metodi ichida `self` parametriga qo'llaniladigan atributlar klassning boshqa metodlarida ham qo'llanilishi kerak bo'lsa, klassga inherit qilingan klasslarda ham `self` parametriga kerak bo'lishi kerak.

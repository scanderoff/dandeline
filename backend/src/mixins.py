class FormCleanMixin:
    def clean_phone(self) -> str:
        phone: str = self.cleaned_data["phone"]
        unmasked: str = "".join(ch for ch in phone if ch.isdigit())

        return unmasked

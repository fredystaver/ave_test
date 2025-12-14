from pydantic import BaseModel, field_validator


class CreatePhoneAddressSchema(BaseModel):
    phone: str
    address: str

    @field_validator("phone")
    def validate_phone(cls, v):
        if v.startswith("+"):
            v = v[1:]

        return v


class GetPhoneAddressSchema(BaseModel):
    phone: str
    address: str


class UpdateAddressSchema(BaseModel):
    address: str

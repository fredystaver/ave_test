from fastapi import APIRouter, status

from api.v1.schemas import CreatePhoneAddressSchema, GetPhoneAddressSchema, UpdateAddressSchema
from app.phone_addresses import PhoneAddressesService

router = APIRouter(
    prefix="/phone_addresses",
    tags=["Phone Addresses"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_phone_address(data: CreatePhoneAddressSchema):
    await PhoneAddressesService.create_phone_address(data=data)


@router.get("/", status_code=status.HTTP_200_OK, response_model=GetPhoneAddressSchema)
async def get_phone_addresses(phone: str):
    address = await PhoneAddressesService.get_phone_address(phone=phone)
    return dict(phone=phone, address=address)


@router.put("/", status_code=status.HTTP_200_OK)
async def update_phone_address(phone: str, data: UpdateAddressSchema):
    await PhoneAddressesService.update_phone_address(phone=phone, data=data)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_phone_address(phone: str):
    await PhoneAddressesService.delete_phone_address(phone=phone)

from fastapi import HTTPException, status

from api.v1.schemas import CreatePhoneAddressSchema, UpdateAddressSchema
from managers.cache import CacheManager


class PhoneAddressesService:

    @classmethod
    async def create_phone_address(cls, data: CreatePhoneAddressSchema) -> None:
        if await cls._check_phone_is_exists(data.phone):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Phone already exists"
            )
        await CacheManager.set(key=data.phone, value=data.address)

    @classmethod
    async def get_phone_address(cls, phone: str) -> str | None:
        if await cls._check_phone_is_exists(phone):
            return await CacheManager.get(key=phone)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Phone does not exist"
        )


    @classmethod
    async def update_phone_address(cls, phone: str, data: UpdateAddressSchema) -> None:
        if await cls._check_phone_is_exists(phone):
            await CacheManager.set(key=phone, value=data.address)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Phone does not exist"
            )


    @classmethod
    async def delete_phone_address(cls, phone: str) -> None:
        if await cls._check_phone_is_exists(phone):
            await CacheManager.delete(key=phone)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Phone does not exist"
            )


    @classmethod
    async def _check_phone_is_exists(cls, phone: str) -> int:
        return await CacheManager.is_exists(phone)

from djangochannelsrestframework.decorators import action
from rest_framework import status


class SubscribeModelMixin:

    @action()
    async def subscribe(self, group_name, **kwargs):
        await self.add_group(group_name)
        return group_name, status.HTTP_201_CREATED

    @action()
    async def unsubscribe(self, group_name, **kwargs):
        await self.remove_group(group_name)
        return group_name, status.HTTP_201_CREATED

    async def send_to(self, event):
        payload = event['message']
        group_name = event['group_name']
        await self.send_json(payload)

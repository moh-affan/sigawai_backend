from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class GenericAsyncBroadcastAPIConsumer(GenericAsyncAPIConsumer):
    async def reply(self,
                    action: str,
                    data=None,
                    errors=None,
                    status=200,
                    request_id=None):
        if errors is None:
            errors = []

        payload = {
            'errors': errors,
            'data': data,
            'action': action,
            'response_status': status,
            'request_id': request_id,
        }
        if self.groups and (action != 'list' and
                            action != 'subscribe' and
                            action != 'unsubscribe'):
            for group_name in self.groups:
                await self.channel_layer.group_send(group_name,
                                                    {'type': 'send_to',
                                                     'message': payload,
                                                     'group_name': group_name})
        else:
            await self.send_json(
                payload
            )

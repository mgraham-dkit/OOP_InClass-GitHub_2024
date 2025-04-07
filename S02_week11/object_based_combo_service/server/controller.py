import datetime as dt

import S02_week11.object_based_combo_service.service.combo_utils as service


class ComboController:
    FORMAT = "%H:%M:%S:%f, %d/%m/%Y"

    def __init__(self):
        self.msg_count = 0

    def handle_echo(self, components: list[str]) -> str:
        if len(components) == 2 and components[1]:
            return components[1]

        return service.INVALID

    def handle_daytime(self, components: list[str]) -> str:
        if len(components) == 1:
            current_date_time = dt.datetime.now()
            return current_date_time.strftime(ComboController.FORMAT)

        return service.INVALID

    def handle_stats(self, components: list[str]) -> str:
        if len(components) == 1:
            return str(self.msg_count)

        return service.INVALID

    def handle_request(self, decoded: str) -> str:
        components = decoded.split(service.DELIMITER)
        self.msg_count += 1
        response = service.INVALID
        match components[0]:
            case service.ECHO:
                response = self.handle_echo(components)
            case service.DAYTIME:
                response = self.handle_daytime(components)
            case service.STATS:
                response = self.handle_stats(components)

        return response
# navigation.py

from evedb import EveDb
from solarmap import SolarMap
from tripwire import Tripwire


class Navigation:
    """
    Navigation
    """
    def __init__(self, gates, system_desc, wh_codes, trip_url, trip_user, trip_pass):
        self.eve_db = EveDb(gates, system_desc, wh_codes)
        self.solar_map = self.eve_db.get_solar_map()
        self.trip_url = None
        self.trip_user = None
        self.trip_pass = None
        self.tripwire_set_login(trip_url, trip_user, trip_pass)

    def reset_chain(self):
        self.solar_map = self.eve_db.get_solar_map()

    def tripwire_set_login(self, trip_url, trip_user, trip_pass):
        self.trip_url = trip_url
        self.trip_user = trip_user
        self.trip_pass = trip_pass

    def tripwire_augment(self, solar_map):
        trip = Tripwire(self.eve_db, self.trip_user, self.trip_pass, self.trip_url)
        return trip.augment_map(solar_map)

    @staticmethod
    def _get_instructions(weight):
        if weight:
            if weight[0] == SolarMap.GATE:
                instructions = "Jump gate"
            elif weight[0] == SolarMap.WORMHOLE:
                [wh_sig, wh_code, _] = weight[1]
                instructions = "Jump wormhole {}[{}]".format(wh_sig, wh_code)
            else:
                instructions = "Instructions unclear, initiate self-destruct"
        else:
            instructions = "Destination reached"

        return instructions

    def route(self, source, destination, avoidance_list, size_restriction):
        source_id = self.eve_db.name2id(source)
        dest_id = self.eve_db.name2id(destination)
        path = self.solar_map.shortest_path(
            source_id,
            dest_id,
            [self.eve_db.name2id(x) for x in avoidance_list],
            size_restriction,
        )

        route = []
        short_format = ""
        prev_gate = None  # Previous gate - will be the system ID of the previous system if connection was a gate

        for idx, x in enumerate(path):
            # Construct route
            if idx < len(path) - 1:
                source = self.solar_map.get_system(x)
                dest = self.solar_map.get_system(path[idx + 1])
                weight = source.get_weight(dest)
            else:
                weight = None
            system_description = list(self.eve_db.system_desc[x])
            system_description.append(Navigation._get_instructions(weight))
            route.append(system_description)

            # Build short format message (traveling between multiple consecutive gates will be denoted as '...')
            if not weight:
                # destination reached
                if prev_gate:
                    if prev_gate != path[idx - 1]:
                        short_format += "...-->"
                short_format += system_description[0]
            else:
                # keep looking
                if weight[0] == SolarMap.WORMHOLE:
                    if prev_gate:
                        if prev_gate != path[idx - 1]:
                            short_format += "...-->"
                    [wh_sig, _, _] = weight[1]
                    short_format += system_description[0] + "[{}]~~>".format(wh_sig)
                    prev_gate = None
                elif weight[0] == SolarMap.GATE:
                    if not prev_gate:
                        short_format += system_description[0] + "-->"
                        prev_gate = path[idx]
                else:
                    # Not supposed to be here
                    short_format += "Where am I?-->"

        return [route, short_format]

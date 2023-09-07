# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class RoomMeetingReservation(object):
    _types = {
        "room_id": str,
        "room_name": str,
        "event_title": str,
        "reserver": str,
        "department_of_reserver": str,
        "guests_number": str,
        "accepted_number": str,
        "event_start_time": str,
        "event_end_time": str,
        "event_duration": str,
        "reservation_status": str,
        "check_in_device": str,
        "room_check_in_status": str,
        "check_in_time": str,
        "is_release_early": str,
        "releasing_person": str,
        "releasing_time": str,
    }

    def __init__(self, d=None):
        self.room_id: Optional[str] = None
        self.room_name: Optional[str] = None
        self.event_title: Optional[str] = None
        self.reserver: Optional[str] = None
        self.department_of_reserver: Optional[str] = None
        self.guests_number: Optional[str] = None
        self.accepted_number: Optional[str] = None
        self.event_start_time: Optional[str] = None
        self.event_end_time: Optional[str] = None
        self.event_duration: Optional[str] = None
        self.reservation_status: Optional[str] = None
        self.check_in_device: Optional[str] = None
        self.room_check_in_status: Optional[str] = None
        self.check_in_time: Optional[str] = None
        self.is_release_early: Optional[str] = None
        self.releasing_person: Optional[str] = None
        self.releasing_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RoomMeetingReservationBuilder":
        return RoomMeetingReservationBuilder()


class RoomMeetingReservationBuilder(object):
    def __init__(self) -> None:
        self._room_meeting_reservation = RoomMeetingReservation()

    def room_id(self, room_id: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.room_id = room_id
        return self

    def room_name(self, room_name: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.room_name = room_name
        return self

    def event_title(self, event_title: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.event_title = event_title
        return self

    def reserver(self, reserver: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.reserver = reserver
        return self

    def department_of_reserver(self, department_of_reserver: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.department_of_reserver = department_of_reserver
        return self

    def guests_number(self, guests_number: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.guests_number = guests_number
        return self

    def accepted_number(self, accepted_number: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.accepted_number = accepted_number
        return self

    def event_start_time(self, event_start_time: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.event_start_time = event_start_time
        return self

    def event_end_time(self, event_end_time: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.event_end_time = event_end_time
        return self

    def event_duration(self, event_duration: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.event_duration = event_duration
        return self

    def reservation_status(self, reservation_status: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.reservation_status = reservation_status
        return self

    def check_in_device(self, check_in_device: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.check_in_device = check_in_device
        return self

    def room_check_in_status(self, room_check_in_status: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.room_check_in_status = room_check_in_status
        return self

    def check_in_time(self, check_in_time: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.check_in_time = check_in_time
        return self

    def is_release_early(self, is_release_early: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.is_release_early = is_release_early
        return self

    def releasing_person(self, releasing_person: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.releasing_person = releasing_person
        return self

    def releasing_time(self, releasing_time: str) -> "RoomMeetingReservationBuilder":
        self._room_meeting_reservation.releasing_time = releasing_time
        return self

    def build(self) -> "RoomMeetingReservation":
        return self._room_meeting_reservation

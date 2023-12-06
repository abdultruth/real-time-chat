from django.test import TestCase
from django.urls import reverse 


from .models import Room

# Create your tests here.
def create_chat(room_name):
   return Room.objects.get_or_create(name=room_name)



class RoomViewTests(TestCase):
   def test_no_repeat_rooms(self):
      """
      If no questions exist, an appropriate message is displayed.
      """
      response = self.client.get(reverse('chat/room_name'))

      self.assertEqual(response, "No Rooms are available.")
      self.assertContains(response, "No Rooms are available.")
      self.assertQuerysetEqual(response.context['room'], [])

   def test_past_room(self):
      """
        Room with a created_at in the past are displayed on the
        index page.
      """

      room = create_chat(room_name="room_name")
      response = self.client.get(reverse('chat/room_name'))
      self.assertQuerySetEqual(
         response.context['room_name'],
      )

      def test_future_room(self):
         pass
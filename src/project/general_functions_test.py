import unittest
from lib.users import Member
from general_functions import add_member, edit_member

class test_member_functions(unittest.TestCase):

    def setUp(self):
        self.member = add_member("Gerard", 987654321, "123 Main St", "Portland", "OR", "97214")

# Ensure add_member() works as expected
    def test_add_member_correct(self):
        member = add_member("Gerard", 987654321, "123 Main St", "Portland", "OR", "97214")
        self.assertEqual(member.name, "Gerard")
        self.assertEqual(member.id, 987654321)
        self.assertEqual(member.address, "123 Main St")
        self.assertEqual(member.city, "Portland")
        self.assertEqual(member.state, "OR")
        self.assertEqual(member.zip, "97214")

# Test edit_member for each attribute
    def test_edit_member_name(self):
        edited_member = edit_member(self.member, "name", "Bartholomew")
        self.assertEqual(edited_member.name, "Bartholomew")

    def test_edit_member_address(self):
        edited_member = edit_member(self.member, "address", "321 New Address")
        self.assertEqual(edited_member.address, "321 New Address")

    def test_edit_member_city(self):
        edited_member = edit_member(self.member, "city", "Boston")
        self.assertEqual(edited_member.city, "Boston")

    def test_edit_member_state(self):
        edited_member = edit_member(self.member, "state", "WA")
        self.assertEqual(edited_member.state, "WA")

    def test_edit_member_zip(self):
        edited_member = edit_member(self.member, "zip", "12345")
        self.assertEqual(edited_member.zip, "12345")

# defect tests
    def test_edit_member_invalid_field(self):
        edited_member = edit_member(self.member, "invalid_field", "Sun Tzu")
        self.assertEqual(edited_member.name, "Gerard") # no changes should be made

    def test_add_member_empty_name(self):
        member = add_member("", 987654321, "123 Main St", "Ghosttown", "OR", "97666")
        self.assertEqual(member.name, "")

    def test_add_member_long_name(self):
        long_name = "A" * 100
        member = add_member(long_name, 987654321, "123 Main St", "Longtown", "OR", "97201")
        self.assertEqual(member.name, long_name[:25])

    def test_add_member_no_zip_code(self):
        member = add_member("Ivy", 987654321, "123 Main St", "New York", "OR", "")
        self.assertEqual(member.zip, "")

    def test_add_member_invalid_zip_code(self):
        member = add_member("Gerard", 987654321, "123 Main St", "Faketown", "OR", "ABCDE")
        self.assertEqual(member.zip, "ABCDE")

    def test_edit_member_to_blank_field(self):
        edited_member = edit_member(self.member, "address", "")
        self.assertEqual(edited_member.address, "")

    def test_edit_member_no_change(self):
        edited_member = edit_member(self.member, "city", "Portland")
        self.assertEqual(edited_member.city, "Portland")

    def test_add_member_with_empty_fields(self):
        member = add_member("", 987654321, "", "", "", "")
        self.assertEqual(member.name, "")
        self.assertEqual(member.address, "")
        self.assertEqual(member.city, "")
        self.assertEqual(member.state, "")
        self.assertEqual(member.zip, "")

    def test_edit_member_with_numeric_city_name(self):
        edited_member = edit_member(self.member, "city", "12345")
        self.assertEqual(edited_member.city, "12345")

    def test_edit_member_case_preservation_in_name(self):
        edited_member = edit_member(self.member, "name", "DaVE123")
        self.assertEqual(edited_member.name, "DaVE123")

    def test_add_member_with_special_characters_in_name(self):
        member = add_member("@lice", 987654321, "Special St", "Symbol City", "NY", "10001")
        self.assertEqual(member.name, "@lice")

    def test_edit_member_with_null_value(self):
        edited_member = edit_member(self.member, "city", None)
        self.assertIsNone(edited_member.city)

    def test_add_member_with_null_values(self):
        member = add_member("Gerard", 987654321, None, None, None, "12345")
        self.assertIsNone(member.address)
        self.assertIsNone(member.city)
        self.assertIsNone(member.state)
        self.assertEqual(member.name, "Jack")
        self.assertEqual(member.zip, "12345")

    def tearDown(self):
        del self.member


if __name__ == "__main__":
    unittest.main()

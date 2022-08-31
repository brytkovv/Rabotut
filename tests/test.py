import os
import sys
import pytest

sys.path.append(os.getcwd())
from run import *
from base import *
from Template.template import *


class TestIncomingFileChecking:
    @pytest.mark.skip(reason='Расположение у всех разное')
    def test_file_existing(self):
        assert Converter._file_existing('C:\environments\TaskRabotut\IncomingData.json')

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            Converter._file_existing('abc')

    @pytest.mark.parametrize('v', [True, 123.45, 12, [12, 34], {}])
    def test_file_string_type_error(self, v):
        with pytest.raises(TypeError):
            Converter._file_existing(v)

    def test_file_format_is_json(self):
        assert Converter._is_file_json_or_raise_type_error('C:\environments\TaskRabotut\IncomingData.json')

    @pytest.mark.parametrize('v', ['a.jpg', 123.45, 12, [12, 34], {}, 'a.jsons'])
    def test_file_format_is_not_json(self, v):
        with pytest.raises(TypeError):
            Converter._is_file_json_or_raise_type_error(v)


class TestIncomingData:
    @pytest.mark.parametrize('v', ['79536762399', ])
    def test_phone_number(self, v):
        assert Contacts.phone_must_be_num(v) == v

    @pytest.mark.parametrize('v', ['7956762399', '795367262399', '7953676.399'])  # TypeError
    def test_incorrect_phone_number(self, v):
        with pytest.raises(ValueError):
            Contacts.phone_must_be_num(v)

    @pytest.mark.parametrize('v', ['ilya.zhuravlev@hrb.software', 'a@a'])
    def test_email(self, v):
        assert Contacts.email_must_contain_at(v) == v

    @pytest.mark.parametrize('v', ['a@', '@a', 'aa'])
    def test_incorrect_email(self, v):
        with pytest.raises(ValueError):
            Contacts.email_must_contain_at(v)

    def test_int_phone_number(self):
        assert type(Contacts.parse_raw(int_phone_in_contacts).phone) == str

    def test_incorrect_coordinates(self):
        with pytest.raises(ValidationError):
            Address.parse_raw(incorrect_coords)

    def test_incorrect_incoming_file(self):
        with pytest.raises(ValidationError):
            IncomingData.parse_raw(incorrect_input)


def test_correct_result_data():
    input_file = IncomingData.parse_raw(original_input)
    result = Converter._file_dependencies_and_return_json(input_file)
    assert result == original_output


if __name__ == '__main__':
    pytest.main()

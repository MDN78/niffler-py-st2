import json
import pytest
from allure import step, epic, suite, title, id, tag
from faker import Faker

from models.user import UserName

# from databases.auth_db import UserDb

pytestmark = [pytest.mark.allure_label("Kafka", label_type="epic")]

KAFKA_TOPIC = 'user'


@epic("[KAFKA][niffler-auth]: Паблишинг сообщений в кафку")
@suite("[KAFKA][niffler-auth]: Паблишинг сообщений в кафку")
class TestAuthRegistrationKafkaTest:
    @id("600001")
    @title("KAFKA: Сообщение с пользователем публикуется в Kafka после успешной регистрации")
    @tag("KAFKA")
    def test_message_should_be_produced_to_kafka_after_successful_registration(self, auth_client, kafka):
        username = Faker().user_name()
        password = Faker().password(special_chars=False)

        topic_partitions = kafka.subscribe_listen_new_offsets("users")

        result = auth_client.register(username, password)
        assert result.status_code == 201

        event = kafka.log_msg_and_json(topic_partitions)

        with step("Check that message from kafka exist"):
            assert event != '' and event != b''

        with step("Check message content"):
            UserName.model_validate(json.loads(event.decode('utf8')))
            assert json.loads(event.decode('utf8'))['username'] == username


    @id("600002")
    @title("KAFKA: Заполнение userdata исключая db")
    @tag("KAFKA")
    def test_message_should_be_produced_to_userdata_after_kafka_event(self, kafka, auth_db, user_db):
        username = Faker().user_name()

        kafka.sent_event(KAFKA_TOPIC, username)

        with step("Check new record in auth db"):
            assert auth_db.get_user_by_username(username) is None

        # with step("Check new record in userdata db"):
        #     assert user_db.get_user(username).username == username

        # user_data = {
        #     "username": "test_user_1",
        #     "firstname": "Test",
        #     "lastname": "User",
        #     "currency": "EUR"
        # }
        # kafka.create_kafka_record(KAFKA_TOPIC, user_data)
        # print(user_data["username"])
        #
        # with step("Check new record in auth db"):
        #     assert auth_db.get_user_by_username(user_data["username"]) is None
        #
        # res = user_db.get_user(user_data["username"])
        # print(res)
        # assert user_db.get_user(username).username == username
        # print(resp)

        # with step("Check new record in userdata db"):
        #     assert user_db.get_user(username).username == username

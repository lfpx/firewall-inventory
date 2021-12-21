from flask_testing import TestCase
from application import app, db
from application.models import Hosts, Rules
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        host = Hosts(host_name="Test_Host_1", host_ip="1.1.1.1")
        rule = Rules(port=80, allow=True, host=host)
        db.session.add(host)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        # self.assertEqual(response.status_code, 200)
        self.assert200(response)

    def test_create_host_get(self):
        response = self.client.get(url_for('create_host'))
        self.assertEqual(response.status_code, 200)

    def test_update_host_get(self):
        response = self.client.get(url_for('update_host', id=1))
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):

    def test_read_hosts(self):
        response = self.client.get(url_for('home'))
        self.assertIn('Test Host 1', str(response.data))

class TestCreate(TestBase):

    def test_create_host(self):
        response = self.client.post(
            url_for('create_host'), 
            json={'host_name':'Test_Host_2','host_ip':'2.2.2.2'},
            follow_redirects=True
        )
        new_host = Hosts.query.get(2)
        self.assertEqual('Test_Host_2', new_host.host_name)
        self.assertEqual('2.2.2.2', new_host.host_ip)

    # This test is creating a dependency between the assertion
    # and the layout of the Home page, if the layout changes and it doesn't
    # show the results anymore this test will fail
    # The previous test doesn't present this problem because it's reading
    # its output directly from the db instead of the server response
    def test_create_host_redirect(self):
        response = self.client.post(
            url_for('create_host'), 
            json={'host_name':'Test_Host_3','host_ip':'3.3.3.3'},
            follow_redirects=True
        )
        self.assertIn('Test_Host_3', str(response.data))
        self.assertIn('3.3.3.3', str(response.data))

class TestUpdate(TestBase):

    def test_update_host(self):
        response = self.client.post(
            url_for('update_host', id=1), 
            json={'host_name':'Test_Host_4','host_ip':'1.1.1.4'},
            follow_redirects=True
        )
        new_host = Hosts.query.get(1)
        self.assertEqual('Test_Host_4', new_host.host_name)
        self.assertEqual('1.1.1.4', new_host.host_ip)

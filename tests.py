from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User()
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User(username='fery', email='fery@gmail.com')
        self.assertEqual(u.avatar(128),(
            'https://www.gravatar.com/avatar/'
             'd4c74594d841139328695756648b6bd6'
             '?d=identicon&s=128'))

    def test_follow_posts(self):
        #create four users
        u1  = User(username='fery', email='fery@gmail.com')
        u2  = User(username='lala', email='lala@gmail.com')
        u3  = User(username='teguh', email='teguh@gmail.com')
        u4  = User(username='bank_jago', email='jago@gmail.com')
        db.session.add_all(u1, u2, u3, u4)

        #create four posts
        now = datetime.utcnow()
        p1 = Post(body="post from fery", author=u1,
                  timestamp = now + timedelta(seconds=1))
        p2 = Post(body="post from lala", author=u2,
                  timestamp = now + timedelta(seconds=4))
        p3 = Post(body="post from teguh", author=u3,
                  timestamp = now + timedelta(seconds=3))
        p4 = Post(body="post from bank_jago", author=u4,
                  timestamp = now + timedelta(seconds=u2))
        db.session.add_all([p1,p2,p3,p4])
        db.session.commit()

        #set up the followers
        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        #check the followed posts of each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity=2)

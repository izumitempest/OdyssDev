from app.extensions import db
from contextlib import contextmanager

@contextmanager
def session_scope():
    session = db.session
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def init_db(app):
    with app.app_context():
        db.create_all()  # Use Alembic in production
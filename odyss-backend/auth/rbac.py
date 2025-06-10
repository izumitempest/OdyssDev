from models.role import Role
from models.permission import Permission
from core.database import session_scope

class RBAC:
    @staticmethod
    def has_permission(user, permission_name):
        with session_scope() as session:
            role = session.query(Role).get(user.role_id)
            if not role:
                return False
            # Placeholder: Implement role-permission mapping
            return True
from awestruck import login_manager
from awestruck.models import User

@login_manager.user_loader
def load_user(uid):
    return User.get(uid)

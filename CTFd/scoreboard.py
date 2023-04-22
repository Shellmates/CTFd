from flask import Blueprint, render_template

from CTFd.utils import config
from CTFd.utils.config.visibility import scores_visible
from CTFd.utils.decorators.visibility import (
    check_account_visibility,
    check_score_visibility,
)
from CTFd.utils.helpers import get_infos
from CTFd.utils.scores import get_standings
from CTFd.utils.user import is_admin

from sqlalchemy import func
from CTFd.models import TeamFieldEntries

scoreboard = Blueprint("scoreboard", __name__)


@scoreboard.route("/scoreboard")
@check_account_visibility
@check_score_visibility
def listing():
    infos = get_infos()

    if config.is_scoreboard_frozen():
        infos.append("Scoreboard has been frozen")

    if is_admin() is True and scores_visible() is False:
        infos.append("Scores are not currently visible to users")

    standings = get_standings()
    # onsite_teams = TeamFieldEntries.query.filter_by(
    #         field_id = 1
    #     ).filter(
    #         func.lower(TeamFieldEntries.value) == func.lower(str(True))
    #     ).all()
    # onsite_ids = [ i.team_id for i in onsite_teams ]
    # return render_template("scoreboard.html", onsite_ids=onsite_ids, standings=standings, infos=infos)
    return render_template("scoreboard.html", standings=standings, infos=infos)

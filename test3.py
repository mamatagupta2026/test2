from app.server.app import app
import uvicorn
from app.core.config import settings


def main():
    uvicorn.run("main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.DEBUG, workers=5)
    print("hello 16 march 2026")
    # For public repos with legacy "pub_acc_*" / "pub_repo_*" IDs, normalize to
                # the "owner_reponame" format that the indexer stores in OpenSearch.
                # Without this, the random-snippet filter sends the old DB value (e.g. "pub_repo_3")
                # but OpenSearch has the normalized value (e.g. "admin_testrepo") → no match.
       print("hello 02 april 2026 4 pm ")


if __name__ == "__main__":
    main()

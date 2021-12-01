import typer 
from ssg.site import site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}

    site(**config).build()


typer.run(main)
import git


branch = format(git.Repo().head.ref.name)

SITE_IMPRINT_DEV = 'dev:' + branch
SITE_IMPRINT_TST = 'tst:' + branch
SITE_IMPRINT_ACC = 'acc'
SITE_IMPRINT_PRD = ''
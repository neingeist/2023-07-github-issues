#!/bin/bash

#gh api /issues \
#  -X "GET" \
#  -H "Accept: application/vnd.github+json" \
#  -H "X-GitHub-Api-Version: 2022-11-28" \
#  -F "filter=created" \
#  > issues.json

GH_USER=neingeist

for type_ in issue pr; do
for field in author assignee; do
  gh api --paginate search/issues \
    -X "GET" \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    -f q="is:$type_ is:open archived:false $field:$GH_USER" \
  > issues-$type_-$field.json
done
done

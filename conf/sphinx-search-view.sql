create or replace
view search_catalog as
select
q.id as question_id,
r.id as response_id,
t.id as tag_id,
q.title as question_title,
q.text as question,
t.text as tag,
r.text as response
from ask_question q
right join ask_response r on r.question_id = q.id
right join ask_question_tags qt on qt.question_id = q.id
join ask_tag t on qt.tag_id = t.id;

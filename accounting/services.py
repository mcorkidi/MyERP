def post_journal_entry(entry):
    entry.posted = True
    entry.save(update_fields=['posted'])

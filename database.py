def init_db(conn):
	conn.execute('''CREATE TABLE IF NOT EXISTS websites (
		id INTEGER PRIMARY KEY AUTOINCREMENT, 
		url text NOT NULL, 
		notifyemail text NOT NULL, 
		created_at timestamp NOT NULL DEFAULT current_timestamp,
		updated_at timestamp NOT NULL DEFAULT current_timestamp)''')
	conn.execute('''
		CREATE TRIGGER IF NOT EXISTS tg_websites_updated_at
		AFTER UPDATE
		ON websites FOR EACH ROW
		BEGIN
			UPDATE websites SET updated_at = current_timestamp
				WHERE id = old.id;
		END
		''')
	conn.execute('''CREATE TABLE IF NOT EXISTS audits (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		code text NOT NULL,
		src_ip text NOT NULL,
		src_port int NOT NULL,
		dst_ip text NOT NULL,
		dst_port int NOT NULL,
		status text,
		section_b text,
		section_f text,
		created_at timestamp DEFAULT current_timestamp
		)''')
	conn.commit()
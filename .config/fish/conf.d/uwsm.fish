if uwsm check may-start; and uwsm select
	exec systemd-cat -t uwsm_start uwsm start default
end


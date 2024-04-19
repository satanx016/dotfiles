const { GLib } = imports.gi;

export const Clock = () => Widget.Box({
    class_name: 'module',
    spacing: 10,
    children: [
        Widget.Label({
            class_name: 'icon',
            label: ''
        }),
        Widget.Label({
            label: GLib.DateTime.new_now_local().format("%H:%M"),
            setup: (self) => self.poll(5000, (self) => {
                self.label = GLib.DateTime.new_now_local().format("%H:%M");
            }),
        })
    ]
})

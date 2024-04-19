import hyprland from "resource:///com/github/Aylur/ags/service/hyprland.js";

let lastTitle = hyprland.active.client.class

const Title = () => {
    return Widget.Box({
        class_name: 'module',
        spacing: 4,
        children: [
            Widget.Label({
                class_name: 'txt-low',
                label: '❖'
            }),
            Widget.Revealer({
                reveal_child: true,
                transitionDuration: 450,
                transition: 'slide_left',
                child: Widget.Label({
                    class_name: 'txt-low',
                    label: lastTitle,
                    setup: (self) => self.hook(hyprland.active, self => {
                        const title = hyprland.active.client.class
                        if (lastTitle != title) {
                            self.get_parent().reveal_child = false
                            Utils.timeout(450, () => {
                                self.label = title.length === 0 ? 'Hyprland' : hyprland.active.client.class
                                self.get_parent().reveal_child = true
                            })
                        }
                        lastTitle = title
                    })
                })
            })
        ]
    })
}

export const WindowTitle = () => {
    return Widget.Box({
        children: [Title()],
    })
}

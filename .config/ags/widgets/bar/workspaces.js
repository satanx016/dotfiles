import hyprland from "resource:///com/github/Aylur/ags/service/hyprland.js";

//A 10 lengthed array 💀 even if i know i will only use 6 workspaces
const ic = [0, '一', '二', '三', '四', '五', '六', '七', '八', '九', '〇']
const maxWorkspaces = 6

const WorkspaceButton = (i) => Widget.EventBox({
    on_primary_click_release: () => hyprland.messageAsync(`dispatch workspace ${i}`),
    child: Widget.Label({
        class_name: 'ws-inactive txt-low',
        label: `${ic[i]}`,
    })
        .hook(hyprland, (button) => {
            const ws_focused = hyprland.active.workspace.id
            const ws_active = hyprland.getWorkspace(i)
            const ws_active_windows = ws_active?.windows || 0
            button.toggleClassName('ws-focused', ws_focused === i)
            button.toggleClassName('ws-active', ws_focused != i && ws_active_windows > 0)
        })
})

export const Workspaces = () => {
    return Widget.Box({
        hpack: 'center',
        spacing: 6,
        children: Array.from({ length: maxWorkspaces }, (_, i) => i + 1)
            .map(i => WorkspaceButton(i)),
    })
}
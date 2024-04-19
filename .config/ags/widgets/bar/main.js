import { Workspaces } from './workspaces.js'
import { WindowTitle } from './windowtitle.js'
import { Indicators } from './indicators.js'
import { Clock } from './clock.js'

const Modules = async () => Widget.Box({
    hpack: 'center',
    children: [
        Indicators(),
        Clock(),
    ]
})

const barContent = Widget.CenterBox({
    class_name: 'bar',
    startWidget: Workspaces(),
    centerWidget: WindowTitle(),
    endWidget: await Modules(),
})

export const Bar = async () => Widget.Window({
    name: 'Bar',
    anchor: ['top', 'left', 'right'],
    exclusivity: 'exclusive',
    child: barContent,
})

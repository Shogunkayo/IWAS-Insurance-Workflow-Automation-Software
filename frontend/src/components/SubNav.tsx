import { useDispatch, useSelector } from "react-redux"
import { setSubView } from "../redux/features/viewSlice"
import { RootState } from "../redux/store"

type Props = {
    navItems: string []
}

const SubNav = (props: Props) => {
    const dispatch = useDispatch()
    const view = useSelector((state: RootState) => state.view)

    return (
        <div className="mx-auto w-fit">
            <button className="hidden bg-primary text-white"></button>
            {props.navItems.map((_, index) => (
                <button key={index} className={`btn-default-white ${view.currentSubView === index && ("bg-primary text-white")}`} onClick={() => dispatch(setSubView(index))}>{props.navItems[index]}</button>
            ))}
        </div>
    )
}

export default SubNav

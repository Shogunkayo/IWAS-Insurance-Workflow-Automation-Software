import { useDispatch } from "react-redux"
import { setSubView } from "../redux/features/viewSlice"

type Props = {
    navItems: string []
}

const SubNav = (props: Props) => {
    const dispatch = useDispatch()

    return (
        <div className="mx-auto w-fit">
            {props.navItems.map((_, index) => (
                <button key={index} className="btn-default-white" onClick={() => dispatch(setSubView(index))}>{props.navItems[index]}</button>
            ))}
        </div>
    )
}

export default SubNav

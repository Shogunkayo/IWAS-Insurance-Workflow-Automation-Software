import Login from "./Login";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "../redux/store";
import { logout, setOpen } from "../redux/features/authSlice";
import axios from "axios";

type Props = {}

const Navbar = (props: Props) => {
    const auth = useSelector((state: RootState) => state.auth)
    const dispatch = useDispatch()

    return (
        <nav className="z-10">
            <div className="bg-primary p-1 relative text-white flex justify-around items-stretch">
                <div>
                    <h2>IWAS</h2>
                </div>
                <div>
                    <button className="btn-default-red">Home</button>
                    <button className="btn-default-red">Personal</button>
                    <button className="btn-default-red">Business</button>
                    <button className="btn-default-red">About Us</button>
                    <button className="btn-default-red">Support</button>
                </div>
                <div className="mt-4">
                    {!auth.user && (
                        <>
                            <button className="btn-white" onClick={() => dispatch(setOpen(true))}>Login</button>
                            <button className="btn-white">Signup</button>
                        </>
                    )}
                    {auth.user && (
                        <>
                            <button className="btn-white" onClick={() => dispatch(logout())}>Logout</button>
                        </>
                    )}
                </div>
            </div>
            {auth.isOpen && (
                <div className="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
                    <div className="relative flex flex-col justify-around">
                        <button
                            type="button"
                            onClick={() => dispatch(setOpen(false))}
                            className="bg-secondary text-white hover:bg-black py-2 px-4 rounded mt-4 top-5 right-5 w-1/2 mx-auto"
                        >
                            Close
                        </button>
                        <Login />
                    </div>
                </div>
            )}
        </nav>
    )
}

export default Navbar

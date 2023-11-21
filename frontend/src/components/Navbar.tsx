import Login from "./Login";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "../redux/store";
import { logout, setOpen } from "../redux/features/authSlice";
import { setView } from "../redux/features/viewSlice";
import { useEffect } from "react";
import SubNav from "./SubNav";
import axios from "axios";

const Navbar = () => {
    const auth = useSelector((state: RootState) => state.auth)
    const curView = useSelector((state: RootState) => state.view.currentView)
    const dispatch = useDispatch()
    
    useEffect(() => {
        if (!auth.user && (curView === 'personal' || curView === 'business' || curView === 'corporate')) {
            dispatch(setView('home'))
            dispatch(setOpen(true))
        }
    }, [auth, curView, dispatch])

    const handleJWTAuth = () => {
        axios.post("http://localhost:5000/verifyAuth", JSON.stringify({"token": "d8sahy823hn12lkndas"}), {headers: {'Content-Type': 'application/json'}})
            .then(response => {
                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
            })
    }
    
    const navItems = ['home', 'personal', 'business', 'corporate', 'about', 'support']
    const homeNavItems = ['Explore Products', 'Grab Deals', 'Bank Smart', 'Knowledge Hub']
    const personalNavItems = ['Purchase Policy', 'Claim Policy', 'Dashboard', 'Account Management']
    const supportNavItems = ['Contact Sales Executive', 'Chatbot']

    return (
        <nav className="z-10 flex flex-col">
            <div className="bg-primary p-1 relative text-white flex justify-around items-stretch">
                <div>
                    <h2>IWAS</h2>
                </div>
                <div className="mt-2">
                    <button className="hidden border-b-2 border-white"></button>
                    {navItems.map((item, index) => (
                        <button key={index} className={`btn-default-red ${curView === item && "border-b-2 border-white"}`} onClick={() => dispatch(setView(item))}>{item.charAt(0).toUpperCase() + item.slice(1)}</button>
                    ))}
                </div>
                <div className="mt-2">
                    <button className="btn-white" onClick={handleJWTAuth}>JWT AUTH</button>
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
            <div className="bg-white shadow-xl p-2 w-full">
                {curView === 'home' && <SubNav navItems={homeNavItems}></SubNav>}
                {curView === 'personal' && <SubNav navItems={personalNavItems}></SubNav>}
                {curView === 'support' && <SubNav navItems={supportNavItems}></SubNav>}
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

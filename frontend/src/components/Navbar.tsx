import { useState } from "react";
import Login from "./Login";

type Props = {}

const Navbar = (props: Props) => {
    const [isModalOpen, setIsModalOpen] = useState(false);

    const openModal = () => {
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    return (
        <nav className="z-10">
            <div className="bg-primary p-1 relative text-white flex justify-around items-stretch">
                <div>
                    <h2>BIG BULLS</h2>
                </div>
                <div>
                    <button className="btn-default-red">Home</button>
                    <button className="btn-default-red">Personal</button>
                    <button className="btn-default-red">Business</button>
                    <button className="btn-default-red">About Us</button>
                    <button className="btn-default-red">Support</button>
                </div>
                <div className="mt-4">
                    <button className="btn-white" onClick={openModal}>Login</button>
                    <button className="btn-white">Signup</button>
                </div>
            </div>
            {isModalOpen && (
                <div className="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
                    <div className="relative flex flex-col justify-around">
                        <button
                            type="button"
                            onClick={closeModal}
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
